import React, { useEffect, useState } from 'react';

function App() {
  const [listings, setListings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://streha.onrender.com/listings/")
      .then((res) => res.json())
      .then((data) => {
        setListings(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch listings:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>🏠 Streha Listings</h1>
      {loading ? (
        <p>Loading listings...</p>
      ) : listings.length > 0 ? (
        <ul>
          {listings.map((listing) => (
            <li key={listing.id}>{listing.title}</li>
          ))}
        </ul>
      ) : (
        <p>No listings found.</p>
      )}
    </div>
  );
}

export default App;
