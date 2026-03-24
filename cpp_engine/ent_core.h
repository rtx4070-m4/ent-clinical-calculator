#ifndef ENT_CORE_H
#define ENT_CORE_H

#include <vector>
#include <numeric>

namespace ENT {
    class AirwayCalculator {
    public:
        static double calculateResistance(double pressure, double flow) {
            if (flow == 0) return 0.0;
            return pressure / flow;
        }
        
        static double calculatePTA(const std::vector<double>& frequencies) {
            double sum = std::accumulate(frequencies.begin(), frequencies.end(), 0.0);
            return sum / frequencies.size();
        }
    };
}

#endif
