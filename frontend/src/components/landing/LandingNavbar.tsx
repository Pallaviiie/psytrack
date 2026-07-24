import { BrainCircuit, Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function LandingNavbar() {
  const [dark, setDark] = useState(false);

  useEffect(() => {
    if (dark) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [dark]);

  return (
    <header className="fixed top-0 left-0 right-0 z-50 border-b border-slate-200 bg-white/70 backdrop-blur-xl dark:border-slate-800 dark:bg-slate-950/70">

      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">

        {/* Logo */}

        <Link to="/" className="flex items-center gap-3">

          <div className="rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 p-3 shadow-lg">

            <BrainCircuit className="text-white" size={28} />

          </div>

          <div>

            <h1 className="text-2xl font-bold">
              PsyTrack
            </h1>

            <p className="text-xs text-slate-500">
              AI Mental Wellness
            </p>

          </div>

        </Link>

        {/* Navigation */}

        <nav className="hidden gap-8 font-medium lg:flex">

          <a href="#home" className="hover:text-violet-600">
            Home
          </a>

          <a href="#features" className="hover:text-violet-600">
            Features
          </a>

          <a href="#how" className="hover:text-violet-600">
            How It Works
          </a>

          <a href="#about" className="hover:text-violet-600">
            About
          </a>

          <a href="#faq" className="hover:text-violet-600">
            FAQ
          </a>

        </nav>

        {/* Right */}

        <div className="flex items-center gap-4">

          <button
            onClick={() => setDark(!dark)}
            className="rounded-xl border p-3 hover:bg-slate-100 dark:hover:bg-slate-900"
          >
            {dark ? <Sun size={20} /> : <Moon size={20} />}
          </button>

          <Link
            to="/login"
            className="rounded-xl border border-violet-600 px-5 py-2 font-medium text-violet-600 hover:bg-violet-600 hover:text-white"
          >
            Login
          </Link>

          <Link
            to="/register"
            className="rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 px-5 py-2 font-medium text-white shadow-lg"
          >
            Sign Up
          </Link>

        </div>

      </div>

    </header>
  );
}