import { FaShieldAlt } from "react-icons/fa";

function Navbar() {
    return (
        <nav className="border-b border-slate-800 bg-slate-900">

            <div className="max-w-6xl mx-auto px-6 py-4 flex items-center gap-3">

                <FaShieldAlt
                    className="text-cyan-400"
                    size={28}
                />

                <div>

                    <h1 className="text-2xl font-bold">
                        Caution-X V2
                    </h1>

                    <p className="text-sm text-gray-400">
                        AI Powered URL Threat Intelligence
                    </p>

                </div>

            </div>

        </nav>
    );
}

export default Navbar;