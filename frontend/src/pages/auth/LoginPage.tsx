import { Link } from "react-router-dom";
import {
  BrainCircuit,
  Mail,
  Lock,
  Eye,
} from "lucide-react";

export default function LoginPage() {
  return (
    <div className="min-h-screen flex bg-gradient-to-br from-violet-50 via-white to-cyan-50">

      {/* LEFT SIDE */}

      <div className="hidden lg:flex lg:w-1/2 items-center justify-center p-10">

        <div className="max-w-lg">

          <div className="flex items-center gap-4">

            <div className="rounded-2xl bg-gradient-to-r from-indigo-600 to-violet-600 p-4 shadow-xl">
              <BrainCircuit className="text-white" size={36} />
            </div>

            <div>

              <h1 className="text-5xl font-extrabold text-slate-900">
                PsyTrack
              </h1>

              <p className="mt-2 text-slate-500 text-lg">
                AI Powered Mental Health Companion
              </p>

            </div>

          </div>

          <div className="mt-14">

            <h2 className="text-5xl font-bold leading-tight text-slate-900">
              Welcome Back 👋
            </h2>

            <p className="mt-6 text-lg leading-8 text-slate-600">
              Track your mental wellness, complete assessments,
              chat with AI, receive personalized recommendations,
              and stay emotionally healthy every day.
            </p>

          </div>

        </div>

      </div>

      {/* RIGHT SIDE */}

      <div className="flex w-full items-center justify-center lg:w-1/2">

        <div className="w-full max-w-md rounded-3xl bg-white p-10 shadow-2xl">

          <h2 className="text-3xl font-bold text-slate-900">
            Login
          </h2>

          <p className="mt-2 text-slate-500">
            Sign in to continue to PsyTrack
          </p>

          {/* Email */}

          <div className="mt-8">

            <label className="mb-2 block font-medium">
              Email Address
            </label>

            <div className="flex items-center rounded-xl border px-4 py-3">

              <Mail className="text-slate-400" size={20} />

              <input
                type="email"
                placeholder="Enter your email"
                className="ml-3 w-full outline-none"
              />

            </div>

          </div>

          {/* Password */}

          <div className="mt-5">

            <label className="mb-2 block font-medium">
              Password
            </label>

            <div className="flex items-center rounded-xl border px-4 py-3">

              <Lock className="text-slate-400" size={20} />

              <input
                type="password"
                placeholder="Enter password"
                className="ml-3 w-full outline-none"
              />

              <Eye
                size={18}
                className="cursor-pointer text-slate-400"
              />

            </div>

          </div>

          {/* Remember */}

          <div className="mt-5 flex items-center justify-between">

            <label className="flex items-center gap-2">

              <input type="checkbox" />

              <span className="text-sm">
                Remember Me
              </span>

            </label>

            <button className="text-sm font-medium text-indigo-600 hover:underline">

              Forgot Password?

            </button>

          </div>

          {/* Login Button */}

          <button
            className="mt-8 w-full rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 py-3 text-lg font-semibold text-white transition hover:scale-[1.02]"
          >
            Login
          </button>

          {/* Divider */}

          <div className="my-8 flex items-center">

            <div className="h-px flex-1 bg-slate-300"></div>

            <span className="px-4 text-slate-400">
              OR
            </span>

            <div className="h-px flex-1 bg-slate-300"></div>

          </div>

          {/* Register */}

          <p className="text-center text-slate-500">

            Don't have an account?{" "}

            <Link
              to="/register"
              className="font-semibold text-indigo-600 hover:underline"
            >
              Create Account
            </Link>

          </p>

        </div>

      </div>

    </div>
  );
}