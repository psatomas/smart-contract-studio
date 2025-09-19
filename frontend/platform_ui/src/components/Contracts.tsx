import { useEffect, useState } from "react";

type Contract = {
  id: number;
  name: string;
  status: string;
};

export default function Contracts() {
  const [contracts, setContracts] = useState<Contract[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/contracts/")
      .then((res) => res.json())
      .then((data) => setContracts(data.contracts))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Contracts</h2>
      {contracts.length === 0 ? (
        <p>No contracts yet</p>
      ) : (
        contracts.map((c) => (
          <div key={c.id} className="card">
            <h3>{c.name}</h3>
            <p>Status: {c.status}</p>
          </div>
        ))
      )}
    </div>
  );
}