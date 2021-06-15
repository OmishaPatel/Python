import pyhash

bit_vector = [0] * 15
print(bit_vector)

# Define fnv and murmur hash functions from pyhash
fnv_hash = pyhash.fnv1_32()
murmur_hash = pyhash.murmur3_32()

# getting output of fnv and murmur 
fnv_hash_pikachu = fnv_hash("pikachu") % 15
murmur_hash_pikachu = murmur_hash("pikachu") % 15
fnv_hash_raichu = fnv_hash("raichu") % 15
murmur_hash_raichu = murmur_hash("raichu") % 15

#print output of fnv and murmur hashes
print("FNV hash output for pikachu: " + str(fnv_hash_pikachu))
print("Murmur hash output for pikachu: " + str(murmur_hash_pikachu))

print("FNV hash output for raichu: " + str(fnv_hash_raichu))
print("Murmur hash output for raichu: " + str(murmur_hash_raichu))

#inserting bits to corresponding location from above hashes
bit_vector[fnv_hash_pikachu] = 1
bit_vector[murmur_hash_pikachu] = 1

bit_vector[fnv_hash_raichu] = 1
bit_vector[murmur_hash_raichu] = 1

print(bit_vector)