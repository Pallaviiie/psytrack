import { ArrowRight } from "lucide-react";
import { Link } from "react-router-dom";

export default function CTA() {
  return (
    <section className="py-28 px-6">

      <div className="max-w-6xl mx-auto rounded-[40px] overflow-hidden">

        <div className="bg-gradient-to-r from-indigo-700 via-violet-600 to-cyan-500 text-white p-16 text-center">

          <h2 className="text-5xl font-bold">
            Start Your Mental Wellness Journey Today
          </h2>

          <p className="mt-6 text-xl text-violet-100 max-w-3xl mx-auto">
            Join thousands of users using AI-powered mental wellness
            monitoring, personalized recommendations, and intelligent
            conversations.
          </p>

          <div className="mt-10 flex justify-center gap-6 flex-wrap">

            <Link
              to="/register"
              className="rounded-xl bg-white text-indigo-700 px-8 py-4 font-semibold hover:scale-105 transition flex items-center gap-2"
            >
              Get Started

              <ArrowRight size={20} />

            </Link>

            <Link
              to="/login"
              className="rounded-xl border border-white px-8 py-4 font-semibold hover:bg-white hover:text-indigo-700 transition"
            >
              Login
            </Link>

          </div>

        </div>

      </div>

    </section>
  );
}