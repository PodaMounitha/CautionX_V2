import { useState } from "react";
import api from "../services/api";

import LoadingSpinner from "./LoadingSpinner";
import ResultCard from "./ResultCard";

function UrlForm() {

    const [url, setUrl] = useState("");

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState(null);

    const [error, setError] = useState("");

    const analyzeUrl = async () => {

        if (url.trim() === "") {

            setError("Please enter a URL.");

            return;
        }

        setError("");

        setLoading(true);

        setResult(null);

        try {

            const response = await api.post("/predict", {

                url

            });

            setResult(response.data);

        }

        catch (err) {

            console.log(err);

            setError("Unable to connect to backend.");

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div className="form-container">

            <h1>

                🛡️ Caution-X V2

            </h1>

            <p>

                AI Powered URL Threat Intelligence Platform

            </p>

            <input

                type="text"

                placeholder="Paste URL here..."

                value={url}

                onChange={(e) => setUrl(e.target.value)}

            />

            <button

                onClick={analyzeUrl}

            >

                Analyze URL

            </button>

            {

                error &&

                <p className="error">

                    {error}

                </p>

            }

            {

                loading &&

                <LoadingSpinner />

            }

            {

                result &&

                <ResultCard result={result} />

            }

        </div>

    );

}

export default UrlForm;