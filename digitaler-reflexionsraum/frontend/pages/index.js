import { useState, useEffect } from "react";

export default function Home() {
  const [dailyQuestion, setDailyQuestion] = useState("");

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    console.log("API URL:", apiUrl); // Debugging: Prüfen, ob die API-URL gesetzt ist

    fetch(`${apiUrl}/api/daily-question`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`API-Fehler: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        if (data && data.question) {
          setDailyQuestion(data.question);
        } else {
          throw new Error("Ungültiges JSON-Format");
        }
      })
      .catch((error) => console.error("API Fehler:", error));
  }, []);

  return (
    <div>
      <h1>Digitaler Reflexionsraum</h1>
      <p data-testid="daily-question">{dailyQuestion || "Lade Frage..."}</p>
    </div>
  );
}