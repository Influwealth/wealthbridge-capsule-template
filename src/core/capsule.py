class Capsule:
    """
    Canonical WealthBridge Capsule Interface.
    All capsules must implement this contract.
    """

    def __init__(self, context: dict):
        """
        context:
          - runtime metadata
          - node identity
          - resource allocations
        """
        self.context = context

    def health(self) -> dict:
        """
        Return capsule health and readiness.
        """
        return {
            "status": "ok",
            "capsule": self.__class__.__name__
        }

    def run(self, inputs: dict) -> dict:
        """
        Execute capsule logic.
        Must be implemented by child capsules.
        """
        raise NotImplementedError("Capsule must implement run()")

    def shutdown(self):
        """
        Graceful shutdown hook.
        """
        pass
