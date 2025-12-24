import yaml

def test_capsule_policy_enforced():
    with open("capsule.yaml") as f:
        spec = yaml.safe_load(f)

    policy = spec.get("policy", {})
    assert policy.get("audit_required") is True
    assert policy.get("pii_allowed") is False
