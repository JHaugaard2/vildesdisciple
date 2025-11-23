"use client";
import { useState, useEffect } from "react";

export default function LiveCamera() {
  const [timestamp, setTimestamp] = useState(Date.now());

  useEffect(() => {
    const interval = setInterval(() => setTimestamp(Date.now()), 1000); // refresh every second
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Live Camera</h1>
      <img
        src={`/photos/latest.jpg?t=${timestamp}`}
        alt="Live feed"
        width={640}
      />
    </div>
  );
}
