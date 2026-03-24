package com.ent.service;

public class CalculationService {
    public double calculatePTA(double[] frequencies) {
        double sum = 0;
        for(double f : frequencies) sum += f;
        return sum / frequencies.length;
    }
    
    public String getRiskCategory(int stopBangScore) {
        if(stopBangScore >= 5) return "HIGH";
        if(stopBangScore >= 3) return "INTERMEDIATE";
        return "LOW";
    }
}
