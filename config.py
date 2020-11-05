branches = ("dev","master")
add_codeowners_file = True
signed_commit = False
branch_rules = { "required_approving_review_count":1,
                 "require_code_owner_reviews":True,
                 "contexts":["CodeQL"],
                 "strict":True
                 }