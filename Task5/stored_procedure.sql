CREATE PROCEDURE ManageBlogPost(
    IN operation VARCHAR(20),
    IN post_id INT,
    IN new_title VARCHAR(255),
    IN new_content TEXT,
    IN user_id INT,
    IN comment_content TEXT,
    IN comment_user_id INT,
    IN comment_id INT
)
BEGIN
    -- Add new post
    IF operation = 'add_post' THEN
        INSERT INTO BlogPosts (title, content, created_at)
        VALUES (new_title, new_content, NOW());
    END IF;

    -- Get post details
    IF operation = 'get_post' THEN
        SELECT title, content, created_at
        FROM BlogPosts
        WHERE id = post_id;
    END IF;

    -- Update post
    IF operation = 'update_post' THEN
        UPDATE BlogPosts
        SET title = new_title, content = new_content
        WHERE id = post_id;
    END IF;

    -- Delete post
    IF operation = 'delete_post' THEN
        DELETE FROM BlogPosts
        WHERE id = post_id;
    END IF;

    -- Add comment
    IF operation = 'add_comment' THEN
        INSERT INTO Comments (id, content, created_at, user_id, post_id)
        VALUES (comment_id, comment_content, NOW(), comment_user_id, post_id);
    END IF;

    -- Delete comment
    IF operation = 'delete_comment' THEN
        DELETE FROM Comments
        WHERE id = comment_id;
    END IF;

    -- Fetch post-related data
    IF operation = 'fetch_post_data' THEN
        SELECT 
            bp.title AS post_title,
            bp.content AS post_content,
            bp.created_at AS post_created_at,
            c.comment_id,
            c.content AS comment_content,
            c.user_id AS comment_user_id,
            c.created_at AS comment_created_at
        FROM BlogPosts bp
        LEFT JOIN Comments c ON bp.post_id = c.post_id
        WHERE bp.post_id = post_id;
    END IF;

END //

DELIMITER ;
