function ResultCard({ result }) {

    if (!result) return null;

    const riskColor = {

        LOW: "#22c55e",

        MEDIUM: "#f59e0b",

        HIGH: "#ef4444"

    };

    return (

        <div className="result-card">

            <h2>

                Analysis Result

            </h2>

            <div
                className="risk-badge"
                style={{
                    background: riskColor[result.risk_level]
                }}
            >

                {result.prediction}

            </div>

            <div className="result-grid">

                <div>

                    <strong>Risk Score</strong>

                    <p>{result.risk_score}/100</p>

                </div>

                <div>

                    <strong>ML Confidence</strong>

                    <p>{result.confidence}%</p>

                </div>

                <div>

                    <strong>Risk Level</strong>

                    <p>{result.risk_level}</p>

                </div>

            </div>

            <h3>

                Recommendation

            </h3>

            <p>

                {result.recommendation}

            </p>

            <h3>

                Reasons

            </h3>

            <ul>

                {result.reasons.map((reason, index) => (

                    <li key={index}>

                        ✔ {reason}

                    </li>

                ))}

            </ul>

            <h3>

                VirusTotal

            </h3>

            <div className="result-grid">

                <div>

                    <strong>Status</strong>

                    <p>

                        {result.virustotal.status}

                    </p>

                </div>

                <div>

                    <strong>Engines</strong>

                    <p>

                        {result.virustotal.engines_detected}

                    </p>

                </div>

                <div>

                    <strong>Harmless</strong>

                    <p>

                        {result.virustotal.harmless}

                    </p>

                </div>

                <div>

                    <strong>Malicious</strong>

                    <p>

                        {result.virustotal.malicious}

                    </p>

                </div>

                <div>

                    <strong>Suspicious</strong>

                    <p>

                        {result.virustotal.suspicious}

                    </p>

                </div>

            </div>

        </div>

    );

}

export default ResultCard;