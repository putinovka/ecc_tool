
#### `ecc.py`
```python
from tinyec import registry
import secrets

class ECCKeyGenerator:
    def __init__(self, curve_name="secp192r1"):
        self.curve = registry.get_curve(curve_name)

    def generate_key_pair(self):
        private_key = secrets.randbelow(self.curve.field.n)
        public_key = private_key * self.curve.g
        return private_key, public_key

    def serialize_public_key(self, public_key):
        return {"x": public_key.x, "y": public_key.y}

    def deserialize_public_key(self, x, y):
        return self.curve.point(x, y)