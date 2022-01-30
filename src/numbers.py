import numpy


class PopulationList(object):
    """
    Class to generate a set of population figures.
    """
    def __init__(self):
        self.rng = numpy.random.default_rng(800)
        self.iterations = 1
        while True:
            self.raw_population_data = self.rng.normal(33, 15, 6)
            self.raw_population_data.sort()
            self.total_raw_pop = numpy.sum(self.raw_population_data)
            if self.correct_population_concentration() \
                    and self.correct_top_two_separation() \
                    and self.constrained_third_highest() \
                    and self.smallest_population_not_too_small():
                break
            # otherwise, go back and roll the dice again...
            self.iterations += 1
        self.populations = self.actual_populations()

    def actual_populations(self) -> list[int]:
        """
        Returns a list of final population figures.
        The raw data are scaled to bring the total back to the base 202 million but with some additional
        randomization to add a little spice.
        """
        randomizers = self.rng.normal(1, 0.05, 6)
        scale_factor = 2.02e8 / self.total_raw_pop
        return [round(pop * scale_factor) for pop in numpy.multiply(self.raw_population_data, randomizers)]

    @property
    def total_population(self) -> int:
        return sum(self.populations)

    def correct_population_concentration(self) -> bool:
        """
        Return true if the ratio between the sum of the two highest populations is within specified limits.
        Concentrate population in the two largest provinces to create an obvious 'big two' but not to the extent that
        the 'big two' render the others entirely insignificant.
        """
        top_pops = sum(self.raw_population_data[4:])
        return 0.475 < top_pops / self.total_raw_pop < 0.525

    def correct_top_two_separation(self) -> bool:
        """
        Return true only if the second-highest population is above the specified fraction of the highest.
        Ensures that the top two populations remain comparable with one another.
        """
        return self.raw_population_data[4] / self.raw_population_data[5] > 0.925

    def constrained_third_highest(self) -> bool:
        """
        Return true only if the third-highest populations is less than the specified fraction of the total.
        Ensures that the third-largest population does not get too close to that of the 'big two' and thus creating a
        'big three'.
        """
        return self.raw_population_data[3] / self.total_raw_pop < (1 / 6)

    def smallest_population_not_too_small(self) -> bool:
        """
        Return true only if the smallest population is above the specified fraction of the total
        Without this threshold the smallest population could be ludicrously small or even negative.
        """
        return self.raw_population_data[0] / self.total_raw_pop > 0.06
