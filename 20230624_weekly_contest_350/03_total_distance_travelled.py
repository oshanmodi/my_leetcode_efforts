class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        injection_initial = mainTank // 5
        maintank_leftover = mainTank % 5
        injection_secondary = (injection_initial + maintank_leftover) // 5
        maintank_leftover = (injection_initial + maintank_leftover) % 5
        injection_tertiary = (injection_secondary + maintank_leftover) // 5
        injection_total = injection_initial + injection_secondary + injection_tertiary
        distance_travelled = (mainTank + min(injection_total, additionalTank)) * 10
        return distance_travelled

    def distanceTraveledBest(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10

    def distanceTraveledSecond(self, mainTank: int, additionalTank: int) -> int:
        count = 0
        tmp = mainTank
        m = 0
        while tmp > 0:
            m_new = (tmp + m) % 5
            tmp = int((tmp + m) / 5)
            count += tmp
            m = m_new
        add = min([count, additionalTank])
        return (mainTank + add) * 10


if __name__ == "__main__":
    sol = Solution()
    # print(sol.distanceTraveled(mainTank=5, additionalTank=10))
    # print(sol.distanceTraveled(mainTank=1, additionalTank=2))
    # print(sol.distanceTraveled(mainTank=9, additionalTank=2))
    print(sol.distanceTraveled(mainTank=29, additionalTank=7))
