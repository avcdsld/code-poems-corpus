function(algo) {
    switch (algo) {
      //   Algorithm-Specific Fields for RSA secret keys:
      //       - multiprecision integer (MPI) of RSA secret exponent d.
      //       - MPI of RSA secret prime value p.
      //       - MPI of RSA secret prime value q (p < q).
      //       - MPI of u, the multiplicative inverse of p, mod q.
      case enums.publicKey.rsa_encrypt:
      case enums.publicKey.rsa_encrypt_sign:
      case enums.publicKey.rsa_sign:
        return [type_mpi, type_mpi, type_mpi, type_mpi];
      //   Algorithm-Specific Fields for Elgamal secret keys:
      //        - MPI of Elgamal secret exponent x.
      case enums.publicKey.elgamal:
        return [type_mpi];
      //   Algorithm-Specific Fields for DSA secret keys:
      //      - MPI of DSA secret exponent x.
      case enums.publicKey.dsa:
        return [type_mpi];
      //   Algorithm-Specific Fields for ECDSA or ECDH secret keys:
      //       - MPI of an integer representing the secret key.
      case enums.publicKey.ecdh:
      case enums.publicKey.ecdsa:
      case enums.publicKey.eddsa:
        return [type_mpi];
      default:
        throw new Error('Invalid public key encryption algorithm.');
    }
  }