import { useEffect, useState } from "react";

export default function Contracts() {
  const [contracts, setContracts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/contracts/")
      .then((res) => res.json())
      .then((data) => setContracts(data.contracts))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Contracts</h2>
      <pre>{JSON.stringify(contracts, null, 2)}</pre>
    </div>
  );
}