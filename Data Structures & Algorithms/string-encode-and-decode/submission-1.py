class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for i in strs:
            encoded_string.append(str(len(i)))
            encoded_string.append("#")
            encoded_string.append(i)

        return "".join(encoded_string);

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start_str = j + 1
            end_str = start_str + length
            decoded_string.append(s[start_str:end_str])

            i = end_str

        return decoded_string;