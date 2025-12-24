from src.core.capsule import Capsule

def test_capsule_interface_exists():
    capsule = Capsule(context={})
    assert hasattr(capsule, "run")
    assert hasattr(capsule, "health")
    assert callable(capsule.run)
    assert callable(capsule.health)
