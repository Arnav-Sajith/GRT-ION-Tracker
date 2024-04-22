import React, { useState, useEffect } from 'react';

function LocationComponent() {
    const [location, setLocation] = useState({ latitude: null, longitude: null });
    const [error, setError] = useState(null);

    useEffect(() => {
        // Check if the Geolocation API is supported
        if (!navigator.geolocation) {
            setError('Geolocation is not supported by your browser');
            return;
        }

        // Define a function to update the state with the new location
        function handleSuccess(position) {
            const { latitude, longitude } = position.coords;
            setLocation({ latitude, longitude });

        }

        // Define a function to handle errors
        function handleError(error) {
            setError(error.message);
        }

        // Request the current position
        // Pass the success and error handlers to the API call
        navigator.geolocation.getCurrentPosition(handleSuccess, handleError);
    }, []); // Empty dependency array means this effect will only run once, like componentDidMount

    // Render the location information or an error message
    return (
        <div>
            <h1>Your Location</h1>
            {error ? (
                <p>Error fetching location: {error}</p>
            ) : (
                <p>Latitude: {location.latitude}, Longitude: {location.longitude}</p>
            )}
        </div>
    );
}

export default LocationComponent;