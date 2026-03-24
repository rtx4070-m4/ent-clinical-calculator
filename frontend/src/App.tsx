import React, { useState } from 'react';
import './App.css';
import PTACalculator from './components/PTACalculator';
import SNOT22Calculator from './components/SNOT22Calculator';

function App() {
  const [activeTab, setActiveTab] = useState('pta');

  return (
    <div className="App min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
      <header className="bg-blue-700 text-white p-4 shadow-md">
        <h1 className="text-2xl font-bold">ENT Clinical Calculator Suite</h1>
        <p className="text-sm opacity-80">Research Grade Toolkit v1.0</p>
      </header>
      
      <nav className="flex border-b border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800">
        <button 
          className={"px-6 py-3 " + (activeTab === 'pta' ? 'border-b-2 border-blue-600 font-bold' : '')}
          onClick={() => setActiveTab('pta')}
        >
          Audiology (PTA)
        </button>
        <button 
          className={"px-6 py-3 " + (activeTab === 'snot22' ? 'border-b-2 border-blue-600 font-bold' : '')}
          onClick={() => setActiveTab('snot22')}
        >
          Rhinology (SNOT-22)
        </button>
      </nav>

      <main className="p-8 max-w-4xl mx-auto">
        {activeTab === 'pta' && <PTACalculator />}
        {activeTab === 'snot22' && <SNOT22Calculator />}
      </main>

      <footer className="mt-12 text-center text-xs text-gray-500 p-4">
        <p>DISCLAIMER: For educational and research purposes only.</p>
      </footer>
    </div>
  );
}

export default App;
