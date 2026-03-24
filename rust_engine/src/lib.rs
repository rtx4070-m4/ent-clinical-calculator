pub struct PatientData {
    pub id: u32,
    pub hearing_thresholds: Vec<f32>,
}

impl PatientData {
    pub fn new(id: u32, thresholds: Vec<f32>) -> Self {
        PatientData { id, hearing_thresholds: thresholds }
    }

    pub fn calculate_pta(&self) -> f32 {
        if self.hearing_thresholds.is_empty() {
            return 0.0;
        }
        let sum: f32 = self.hearing_thresholds.iter().sum();
        sum / self.hearing_thresholds.len() as f32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_pta_calculation() {
        let patient = PatientData::new(1, vec![20.0, 25.0, 30.0]);
        assert_eq!(patient.calculate_pta(), 25.0);
    }
}
