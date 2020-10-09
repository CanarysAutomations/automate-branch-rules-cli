branch_name = "master"
signed_commit = os.getenv(REQUIRED_SIGNED_COMMITS")
branch_rules = { "required_approving_review_count":1,
                 "enforce_admins":True,
                 "dismiss_stale_reviews":True,
                 "user_push_restrictions":["User1","User2"],
                 "strict":False,
                 "contexts":["StatusCheck1","StatusCheck2"]
                 }
