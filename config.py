"""Change the config values."""
branches = ('master', 'dev')  # Note: Single element requires a comma at end.
add_codeowners_file = True
signed_commit = False
branch_rules = {"required_approving_review_count": 1,
                "require_code_owner_reviews": True,
                "contexts": ["CodeQL"],
                "strict": True
                }
