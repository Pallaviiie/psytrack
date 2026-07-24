import {
  Bell,
  Moon,
  Search,
  Sun,
  UserCircle2,
  LogIn,
  UserPlus,
} from "lucide-react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  const [darkMode, setDarkMode] = useState(false);

  // later this will come from JWT authentication
  const token = localStorage.getItem("access_token");

  // later this will come from backend
  const userName = localStorage.getItem("user_name") || "User";

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [darkMode]);

  return (
    <header className="sticky top-0 z-50 flex h-20 items-center justify-between border-b border-slate-200 bg-white/80 px-8 backdrop-blur-md dark:border-slate-800 dark:bg-slate-950/80">

      {/* Left */}

      <div>
        <h1 className="text-3xl font-bold">
          Welcome Back 👋
        </h1>

        <p className="text-slate-500">
          Monitor your mental wellness today.
        </p>
      </div>

      {/* Right */}

      <div className="flex items-center gap-4">

        {/* Search */}

        <div className="relative hidden lg:block">
          <Search
            className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
            size={18}
          />

          <input
            placeholder="Search..."
            className="w-72 rounded-xl border border-slate-300 bg-slate-100 py-2 pl-10 pr-4 outline-none focus:border-violet-500 dark:border-slate-700 dark:bg-slate-900"
          />
        </div>

        {/* Notification */}

        <button className="rounded-xl bg-slate-100 p-3 hover:bg-slate-200 dark:bg-slate-900 dark:hover:bg-slate-800">
          <Bell size={20} />
        </button>

        {/* Theme */}

        <button
          onClick={() => setDarkMode(!darkMode)}
          className="rounded-xl bg-slate-100 p-3 hover:bg-slate-200 dark:bg-slate-900 dark:hover:bg-slate-800"
        >
          {darkMode ? <Sun size={20} /> : <Moon size={20} />}
        </button>

        {/* Authentication */}

        {!token ? (
          <div className="flex items-center gap-3">

            <Link
              to="/login"
              className="flex items-center gap-2 rounded-xl border border-violet-600 px-5 py-2 font-medium text-violet-600 transition hover:bg-violet-600 hover:text-white"
            >
              <LogIn size={18} />
              Login
            </Link>

            <Link
              to="/register"
              className="flex items-center gap-2 rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 px-5 py-2 font-medium text-white shadow-lg transition hover:scale-105"
            >
              <UserPlus size={18} />
              Sign Up
            </Link>

          </div>
        ) : (
          <div className="flex items-center gap-3 rounded-xl bg-slate-100 px-4 py-2 dark:bg-slate-900">

            <UserCircle2
              size={42}
              className="text-violet-600"
            />

            <div>

              <h3 className="font-semibold">
                {userName}
              </h3>

              <p className="text-xs text-slate-500">
                Welcome Back!
              </p>

            </div>

          </div>
        )}

      </div>
    </header>
  );
}