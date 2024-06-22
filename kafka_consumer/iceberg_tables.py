ice_tables = {
    "commits": """
                create table if not exists bronze.commits (
                    owner STRING,
                    repo STRING,
                    commit_sha STRING,
                    url STRING,
                    comment_count INT,
                    commit_message STRING,
                    author_id LONG,
                    author_login STRING,
                    author_type STRING,
                    author_name STRING,
                    commit_author_date TIMESTAMP,
                    commit_author_email STRING,
                    committer_id LONG,
                    committer_login STRING,
                    committer_type STRING,
                    committer_name STRING,
                    commit_committer_date TIMESTAMP,
                    commit_committer_email STRING,
                    commit_verification_reason STRING,
                    commit_verification_verified BOOLEAN,
                    response STRING,
                    created_date TIMESTAMP
               )
               using iceberg
               location '{}'
               partitioned by (owner, days(commit_author_date));
                """,
    "issues": """
                create table if not exists bronze.issues (
                    owner STRING,
                    repo STRING,
                    id BIGINT,
                    number BIGINT,
                    title STRING,
                    state STRING,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP,
                    closed_at TIMESTAMP,
                    comments BIGINT,
                    draft BOOLEAN,
                    author_association STRING,
                    user_id BIGINT,
                    label_id BIGINT,
                    repository_url STRING,
                    total_count INT,
                    plus1 INT,
                    minus1 INT,
                    laugh INT,
                    hooray INT,
                    confused INT,
                    heart INT,
                    rocket INT,
                    eyes INT,
                    response STRING,
                    created_date TIMESTAMP
                )
                using iceberg
                location '{}'
                partitioned by (owner, days(created_at));
                """
}