import React, { useState, useEffect } from 'react';
import { Sun, CloudRain, CloudSnow, AlertTriangle } from 'lucide-react';
import './App.css';

const API_KEY = 'YOUR_OPENWEATHER_API_KEY';

const WeatherApp = () => {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState('');

  const fetchWeather = async () => {
    try {
      setError('');
      const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=eeaedeb8381d95a36364265f0b07030f`)

      if (!response.ok) throw new Error('City not found');
      const data = await response.json();
      setWeather(data);
    } catch (err) {
      setWeather(null);
      setError(err.message);
    }
  };

  useEffect(() => {
    if (city) fetchWeather();
  }, []); // eslint-disable-line

  const getWeatherIcon = (main) => {
    switch (main) {
      case 'Clear': return <Sun size={48} />;
      case 'Rain': return <CloudRain size={48} />;
      case 'Snow': return <CloudSnow size={48} />;
      default: return <Sun size={48} />;
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">Weather App</h1>
      <div className="input-group">
        <input
          type="text"
          placeholder="Enter city name"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />
        <button onClick={fetchWeather}>Get Weather</button>
      </div>

      {error && (
        <div className="error">
          <AlertTriangle size={24} /> {error}
        </div>
      )}

      {weather && (
        <div className="weather-card">
          <h2>{weather.name}, {weather.sys.country}</h2>
          <div className="weather-main">
            {getWeatherIcon(weather.weather[0].main)}
            <p>{weather.weather[0].main}</p>
          </div>
          <p>Temperature: {weather.main.temp}&deg;C</p>
          <p>Humidity: {weather.main.humidity}%</p>
          <p>Wind Speed: {weather.wind.speed} m/s</p>
        </div>
      )}
    </div>
  );
};

export default WeatherApp;
