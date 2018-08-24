from re import findall as regex

def find_keys(dict_dir, regex_pattern, string, checkall = False):
    _matching = []
    with open(dict_dir, "rb") as _dict:
        while True:
            line = _dict.readline().strip()
            if not line:
                return _matching
            line = line.decode("utf-8")
            text = xor_string(line, string)
            lst = regex(regex_pattern, text)
            if lst:
                _matching.append(line)
                if not checkall:
                    return _matching

def xor_string(key, string):
    l = len(string)
    key_len = len(key)
    _out = ""
    for i in range(0, l):
        key_index = (i % key_len)
        _out += chr(ord(string[i]) ^ ord(key[key_index]))
    return _out

if __name__ == "__main__":
    encrypted = xor_string("1337", "helloworld{wooop_iMATCH_ze_pattern}")
    keys = find_keys("/mnt/d/_root/data/rockyou", "{.*}", encrypted)
    print(keys)