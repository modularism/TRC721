class Deploy(bt.Synapse):
    # Key of data
    tick: str = "" 
    max: int = -1
    lim: int = -1
    dec: int = -1
    
    required_hash_fields: typing.List[str] = ["tick", "max"]

    # Deserialize responses
    def deserialize(self) -> str:
        return self.tick
