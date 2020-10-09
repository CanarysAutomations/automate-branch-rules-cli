branch_name = "master" # Provide name of the branch
signed_commit = True # Mark True/False if required signed commits as branch rule

# Refer README.md for configuring other rules
branch_rules = { "required_approving_review_count":1,
                 "enforce_admins":True,
                 "dismiss_stale_reviews":True,
                 "user_push_restrictions":["User1","User2"],
                 "strict":False,
                 "contexts":["Status_Check1","Status_Check2"]
                 }
