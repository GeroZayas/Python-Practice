import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            if len(s1) > len(s2):
                return False

            s1Count, s2Count = [0] * 26, [0] * 26
            for i in range(len(s1)):
                s1Count[ord(s1[i]) - ord("a")] += 1
                s2Count[ord(s2[i]) - ord("a")] += 1

            matches = 0
            for i in range(26):
                matches += 1 if s1Count[i] == s2Count[i] else 0

            l = 0
            for r in range(len(s1), len(s2)):
                if matches == 26:
                    return True

                index = ord(s2[r]) - ord("a")
                s2Count[index] += 1
                if s1Count[index] == s2Count[index]:
                    matches += 1
                elif s1Count[index] + 1 == s2Count[index]:
                    matches -= 1

                index = ord(s2[l]) - ord("a")
                s2Count[index] -= 1
                if s1Count[index] == s2Count[index]:
                    matches += 1
                elif s1Count[index] - 1 == s2Count[index]:
                    matches -= 1
                l += 1
            return matches == 26

    return Solution,


@app.cell
def __(Solution):
    solution = Solution()
    s1 = "abc"
    s2 = "lecabee"
    s3 = "gero"
    s4 = "relojero"
    return s1, s2, s3, s4, solution


@app.cell
def __(s1, s2, solution):
    solution.checkInclusion(s1,s2)
    return


@app.cell
def __(solution):
    check = solution.checkInclusion
    return check,


@app.cell
def __(check, s3, s4):
    check(s3,s4)
    return


@app.cell
def __():
    s5, s6 = "Aaa", "Abadacadabra"
    return s5, s6


@app.cell
def __(check, s5, s6):
    check(s6,s5)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
