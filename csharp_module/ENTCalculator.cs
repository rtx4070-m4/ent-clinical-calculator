using System;

namespace ENT.Calculators {
    public class StopBangCalculator {
        public class Result {
            public int Score { get; set; }
            public string RiskLevel { get; set; }
        }

        public static Result Calculate(bool snoring, bool tired, bool apnea, bool pressure, double bmi, int age, double neck, string gender) {
            int score = 0;
            if(snoring) score++;
            if(tired) score++;
            if(apnea) score++;
            if(pressure) score++;
            if(bmi > 35) score++;
            if(age > 50) score++;
            if(neck > 40) score++;
            if(gender.ToLower() == "male") score++;
            string risk = score >= 5 ? "High" : (score >= 3 ? "Intermediate" : "Low");
            return new Result { Score = score, RiskLevel = risk };
        }
    }
}
