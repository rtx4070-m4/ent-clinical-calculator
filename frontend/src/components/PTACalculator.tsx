import React, { useState } from 'react';

const PTACalculator = () => {
  const [inputs, setInputs] = useState({
    left_500: '', left_1000: '', left_2000: '',
    right_500: '', right_1000: '', right_2000: ''
  });
  const [result, setResult] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const lAvg = (Number(inputs.left_500) + Number(inputs.left_1000) + Number(inputs.left_2000)) / 3;
    const rAvg = (Number(inputs.right_500) + Number(inputs.right_1000) + Number(inputs.right_2000)) / 3;
    setResult({ left: lAvg.toFixed(2), right: rAvg.toFixed(2) });
  };

  const handleChange = (e) => {
    setInputs({...inputs, [e.target.name]: e.target.value});
  };

  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
      <h2 className="text-xl font-semibold mb-4">Pure Tone Average (PTA)</h2>
      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
        <div className="col-span-2 font-bold text-blue-600">Left Ear (dB HL)</div>
        {['500', '1000', '2000'].map(freq => (
          <input key={"l" + freq} name={"left_" + freq} type="number" placeholder={freq + " Hz"} onChange={handleChange} className="border p-2 rounded dark:bg-gray-700"/>
        ))}
        <div className="col-span-2 font-bold text-red-600 mt-2">Right Ear (dB HL)</div>
        {['500', '1000', '2000'].map(freq => (
          <input key={"r" + freq} name={"right_" + freq} type="number" placeholder={freq + " Hz"} onChange={handleChange} className="border p-2 rounded dark:bg-gray-700"/>
        ))}
        <button type="submit" className="col-span-2 bg-blue-600 text-white p-2 rounded hover:bg-blue-700">Calculate</button>
      </form>
      {result && (
        <div className="mt-6 p-4 bg-gray-100 dark:bg-gray-700 rounded">
          <p>Left PTA: <strong>{result.left} dB</strong></p>
          <p>Right PTA: <strong>{result.right} dB</strong></p>
        </div>
      )}
    </div>
  );
};

export default PTACalculator;
