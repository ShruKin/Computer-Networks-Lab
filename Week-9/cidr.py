import copy

in_ip = input("Enter CIDR Address: ")

blocks, cidr = in_ip.split("/")
blocks = blocks.split(".")
cidr = int(cidr)

blocks_bin = list(
    map(lambda b: bin(int(b)).replace("0b", "").zfill(8), blocks))

to_cover = 32 - cidr

start_ip = copy.deepcopy(blocks_bin)
end_ip = copy.deepcopy(blocks_bin)
i = 0
while to_cover > 8:
    start_ip[3-i] = "0" * 8
    end_ip[3-i] = "1" * 8
    to_cover -= 8
    i += 1

splitf = blocks_bin[3-i][:8-to_cover]
splite = blocks_bin[3-i][-to_cover:]

start_ip[3-i] = splitf + "0"*to_cover
end_ip[3-i] = splitf + "1"*to_cover

start_ip = ".".join([str(int(i, 2)) for i in start_ip])
end_ip = ".".join([str(int(i, 2)) for i in end_ip])


print(start_ip)
print(end_ip)
print("No of IPs:", 2 ** (32-cidr))
