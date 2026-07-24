import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "sonner";

import { registerUser } from "@/api/auth";

import {
  BrainCircuit,
  User,
  Mail,
  Lock,
  Eye,
} from "lucide-react";

export default function RegisterPage() {
  const navigate = useNavigate();

  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleRegister = async () => {
    if (
      !formData.full_name ||
      !formData.email ||
      !formData.password ||
      !formData.confirmPassword
    ) {
      toast.error("Please fill all fields");
      return;
    }

    if (formData.password !== formData.confirmPassword) {
      toast.error("Passwords do not match");
      return;
    }

    try {
      setLoading(true);

      await registerUser({
        full_name: formData.full_name,
        email: formData.email,
        password: formData.password,
      });

      toast.success("Registration Successful");

      navigate("/login");
    } catch (error: any) {
      toast.error(
        error?.response?.data?.detail ||
          "Registration Failed"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex bg-gradient-to-br from-violet-50 via-white to-cyan-50">
      {/* LEFT PANEL */}

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

              <p className="mt-2 text-lg text-slate-500">
                AI Powered Mental Health Companion
              </p>
            </div>
          </div>

          <div className="mt-14">
            <h2 className="text-5xl font-bold leading-tight text-slate-900">
              Join PsyTrack 💜
            </h2>

            <p className="mt-6 text-lg leading-8 text-slate-600">
              Create your account to track your mental wellness,
              chat with AI, complete assessments and receive
              personalized recommendations.
            </p>
          </div>
        </div>
      </div>

      {/* RIGHT PANEL */}

      <div className="flex w-full items-center justify-center lg:w-1/2">
        <div className="w-full max-w-md rounded-3xl bg-white p-10 shadow-2xl">
          <h2 className="text-3xl font-bold text-slate-900">
            Create Account
          </h2>

          <p className="mt-2 text-slate-500">
            Sign up to start your wellness journey
          </p>

          {/* Full Name */}

          <div className="mt-8">
            <label className="mb-2 block font-medium">
              Full Name
            </label>

            <div className="flex items-center rounded-xl border px-4 py-3">
              <User className="text-slate-400" size={20} />

              <input
                type="text"
                name="full_name"
                value={formData.full_name}
                onChange={handleChange}
                placeholder="Enter your full name"
                className="ml-3 w-full outline-none"
              />
            </div>
          </div>

          {/* Email */}

          <div className="mt-5">
            <label className="mb-2 block font-medium">
              Email Address
            </label>

            <div className="flex items-center rounded-xl border px-4 py-3">
              <Mail className="text-slate-400" size={20} />

              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
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
                name="password"
                value={formData.password}
                onChange={handleChange}
                placeholder="Create password"
                className="ml-3 w-full outline-none"
              />

              <Eye
                className="cursor-pointer text-slate-400"
                size={18}
              />
            </div>
          </div>

          {/* Confirm Password */}

          <div className="mt-5">
            <label className="mb-2 block font-medium">
              Confirm Password
            </label>

            <div className="flex items-center rounded-xl border px-4 py-3">
              <Lock className="text-slate-400" size={20} />

              <input
                type="password"
                name="confirmPassword"
                value={formData.confirmPassword}
                onChange={handleChange}
                placeholder="Confirm password"
                className="ml-3 w-full outline-none"
              />

              <Eye
                className="cursor-pointer text-slate-400"
                size={18}
              />
            </div>
          </div>

                    {/* Terms */}

          <div className="mt-5 flex items-start gap-2">
            <input type="checkbox" className="mt-1" />

            <span className="text-sm text-slate-500">
              I agree to the
              <span className="cursor-pointer font-semibold text-indigo-600">
                {" "}
                Terms & Conditions
              </span>
              {" "}and
              <span className="cursor-pointer font-semibold text-indigo-600">
                {" "}
                Privacy Policy
              </span>
            </span>
          </div>

          {/* Register Button */}

          <button
            onClick={handleRegister}
            disabled={loading}
            className="mt-8 w-full rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 py-3 text-lg font-semibold text-white transition hover:scale-[1.02] disabled:opacity-60"
          >
            {loading
              ? "Creating Account..."
              : "Create Account"}
          </button>

          {/* Divider */}

          <div className="my-8 flex items-center">
            <div className="h-px flex-1 bg-slate-300"></div>

            <span className="px-4 text-slate-400">
              OR
            </span>

            <div className="h-px flex-1 bg-slate-300"></div>
          </div>

          {/* Login */}

          <p className="text-center text-slate-500">
            Already have an account?{" "}

            <Link
              to="/login"
              className="font-semibold text-indigo-600 hover:underline"
            >
              Login
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}