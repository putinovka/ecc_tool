from ecc import ECCKeyGenerator

def main():
    print("Welcome to the Elliptic Curve Cryptography (ECC) Key Generator!")
    ecc = ECCKeyGenerator()

    private_key, public_key = ecc.generate_key_pair()
    serialized_public_key = ecc.serialize_public_key(public_key)

    print("\nPrivate Key:", private_key)
    print("Public Key:", serialized_public_key)

    # Deserialize public key
    deserialized_public_key = ecc.deserialize_public_key(serialized_public_key["x"], serialized_public_key["y"])
    print("\nDeserialized Public Key:", deserialized_public_key)

if __name__ == "__main__":
    main()