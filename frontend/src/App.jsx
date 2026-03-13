
import React, { useState } from "react";
import axios from "axios";

const api = axios.create({ baseURL: "http://127.0.0.1:8000" });

export default function App() {
  const [files, setFiles] = useState([]);
  const [q, setQ] = useState("");
  const [ans, setAns] = useState("");
  const [ev, setEv] = useState([]);

  async function ingest() {
    const fd = new FormData();
    files.forEach(f => fd.append("files", f));
    await api.post("/ingest", fd);
    alert("Ingested");
  }

  async function ask() {
    const r = await api.post("/query", { question: q });
    setAns(r.data.answer);
    setEv(r.data.evidence);
  }

  return (
    <div style={{padding:30}}>
      <h1>Grounded Intelligence</h1>
      <input type="file" multiple onChange={e=>setFiles([...e.target.files])}/>
      <button onClick={ingest}>Ingest</button>
      <hr/>
      <input value={q} onChange={e=>setQ(e.target.value)} style={{width:"100%"}}/>
      <button onClick={ask}>Ask</button>
      <h3>Answer</h3>{ans}
      <h3>Evidence</h3>
      {ev.map((e,i)=>(<pre key={i}>{e.source} p{e.page}\n{e.text}</pre>))}
    </div>
  );
}
