CREATE PROCEDURE ManageBlogPost
     @Operation VARCHAR(25),
     @PostId INT,
	 @UserID INT,
     @NewTitle VARCHAR(255),
     @NewContent TEXT,
     @CommentContent TEXT,
     @CommentID INT,
	 @CommentUserID INT
AS
BEGIN
    -- Add new post
    IF @Operation = 'add_post'
	BEGIN
        INSERT INTO BlogPosts (PostID, UserID, Title, Content)
        VALUES (@PostId , @UserID, @NewTitle, @NewContent);
    END;

    -- Get post details
    IF @Operation = 'get_post'
	BEGIN
        SELECT Title, Content, Created_at
        FROM BlogPosts
        WHERE PostID = @PostId;
    END;

    -- Update post
    IF @Operation = 'update_post'
	BEGIN
        UPDATE BlogPosts
        SET Title = @NewTitle, Content = @NewContent
        WHERE PostID = @PostId;
    END;

    -- Delete post
    IF @Operation = 'delete_post' 
	BEGIN
        DELETE FROM BlogPosts
        WHERE PostID = @PostId;
    END;

    -- Add comment
    IF @Operation = 'add_comment'
	BEGIN
        INSERT INTO Comments (CommentID, CommentContent, UserID, PostID)
        VALUES (@CommentID, @CommentContent, @UserID, @PostId);
    END;

    -- Delete comment
    IF @Operation = 'delete_comment'
	BEGIN
        DELETE FROM Comments
        WHERE CommentID = @CommentID
    END ;

    -- Fetch post-related data
    IF @Operation = 'fetch_post_data'
	BEGIN
        SELECT 
            bp.Title AS PostTitle,
            bp.Content AS PostContent,
            bp.Created_at AS PostCreatedAt,
            c.CommentID,
            c.CommentContent,
            c.UserID AS CommentUserID,
            c.CreatedAt AS CommentCreatedAt
        FROM BlogPosts bp
        LEFT JOIN Comments c ON bp.PostID = c.PostID
        WHERE bp.PostID = @PostId
    END ;
END;

 -- Example usage
EXEC ManageBlogPost 'add_post', 10, 2, 'A7', 'A7', NULL, NULL, NULL 
EXEC ManageBlogPost 'fetch_post_data', 2, NULL, NULL, NULL, NULL, NULL, NULL
EXEC ManageBlogPost 'add_comment', NULL, 2, NULL, NULL, 'A7', 10, NULL