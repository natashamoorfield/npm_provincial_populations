# Clamarendian Population
This project is part of the world building for the novel _Visions in Blue_ by Natalya Petrovna Moorfield and collaborators. The script herein calculates the population figures for each of the Six Provinces of human civilization on Calmarendi.
## Actual Population Figures
Although the Guilds, local and provincial governments, and anyone else with a need to know such information will be able, one way or another, to estimate population figures, ultimately they are just that, estimates. Even the robots, with their access to advanced data analysis tools or a complete census - subject to errors, misrepresentations, omissions and evasion - can never arrive at figures that are anything other than estimates, even if they might be very good estimates.

Nevertheless, there must be actual, exact numbers that can be placed on the populations of each province at any given moment in time. Calculating those numbers is what this script is all about.

## How We Calculate the Numbers
### In-World Assumptions
#### Snapshot Time
The calculated figures represent the population of the Western Provinces at the start of Day One of the Apocalypse: the day on which Jennifer and Colette arrive on Calmarendi.
#### Who We Have Included in the Count
The figures currently only include those people who might be considered ordinarily resident (however that term is defined) within the boundaries of one of the Six Provinces.  They do not include anyone who is permanently resident elsewhere on Calmarendi nor anyone resident in any of the subterranean facilities of the Younger Humans on Calmarendi.

### Creative Constraints
This is where we step beyond unreality and set the constraints that will shape our creation even though we still want some elements of random variability to enter into our calculations.
#### Long Term Average Population
Although the meaning of "long-term" is not defined, the stable, long-term average population of the Western Provinces has been determined at 2.02 x 10^8 (202 million).
#### Long Term Provincial Averages
Each province is assumed to also have a stable, long-term average around which the population fluctuates. The meaning of long-term and the actual values of the averages are not defined. However the ranking of the provinces according to these averages is defined as being (smallest to largest) Mercia, Avon, Bohemia, Wessex, Victoria, Eden.
#### Relative Population Distributions
- Between 47.5% and 52.5% of the total population of the Western Provinces is resident in either Eden or Victoria.
- The population of Victoria is greater than 92.5% but not greater than 100%  that of Eden.
- The population of Wessex is not more than one-sixth of the total.
- The population of Mercia is greater than 6% of the total.

### Calculation
#### Initial Determination
A set of population figures that conform to the above constraints  and which, in particular, yield a total population of exactly 202 million is generated randomly.
#### Further Randomization
The population of each province is then adjusted by its own, additional randomizing factor of plus or minus a few percent. This will yield a random deviation of total population away from the 202 million average.  It may also result in some or all of the base constraints for the populations of individual provinces, including that of population ranking, being breached; this is intentional - a feature not a bug.