

with    
    final as (
        select
            repo,
            committer_name,
            num_commits
        from
            {{ ref('int_num_committer_commits') }}
)
select
    *
from
    final
order by
    repo,
    num_commits desc