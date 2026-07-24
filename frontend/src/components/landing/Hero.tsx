import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { BrainCircuit, ShieldCheck, MessageCircleHeart } from "lucide-react";
import FadeInSection from "@/components/common/FadeInSection";

export default function Hero() {
  return (
    <FadeInSection>
      <section className="min-h-screen bg-gradient-to-br from-violet-50 via-white to-blue-50 flex items-center">

        <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">

          {/* Left Content */}

          <motion.div
            initial={{ opacity: 0, x: -60 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
          >
            <span className="inline-flex items-center gap-2 bg-violet-100 text-violet-700 px-4 py-2 rounded-full font-medium mb-6">

              <BrainCircuit size={18} />

              AI Powered Mental Wellness

            </span>

            <h1 className="text-5xl lg:text-6xl font-extrabold text-slate-900 leading-tight">

              Your Personal

              <span className="text-violet-600">

                {" "}AI Mental Health{" "}

              </span>

              Companion

            </h1>

            <p className="mt-8 text-lg text-slate-600 leading-8">

              PsyTrack helps you monitor emotional wellbeing,
              assess your mental health, chat with an intelligent
              AI therapist, receive personalized wellness
              recommendations and access emergency support
              whenever you need it.

            </p>

            <div className="flex flex-wrap gap-5 mt-10">

              <Link
                to="/register"
                className="bg-violet-600 hover:bg-violet-700 text-white px-8 py-4 rounded-xl font-semibold transition duration-300 shadow-lg"
              >
                Get Started
              </Link>

              <Link
                to="/login"
                className="border border-violet-600 text-violet-600 hover:bg-violet-50 px-8 py-4 rounded-xl font-semibold transition"
              >
                Login
              </Link>

            </div>

          </motion.div>

          {/* Right Illustration */}

          <motion.div
            initial={{ opacity: 0, x: 60 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            className="relative"
          >

            <div className="bg-white rounded-3xl shadow-2xl p-8">

              <div className="space-y-6">

                <div className="flex items-center gap-4">

                  <div className="bg-violet-100 p-4 rounded-2xl">

                    <MessageCircleHeart
                      className="text-violet-600"
                      size={30}
                    />

                  </div>

                  <div>

                    <h3 className="font-bold text-xl">

                      AI Chat Support

                    </h3>

                    <p className="text-gray-500">

                      Talk anytime, anywhere.

                    </p>

                  </div>

                </div>

                <div className="bg-violet-50 rounded-2xl p-6">

                  <p className="font-semibold text-violet-700">

                    😊 Mood Today

                  </p>

                  <h2 className="text-4xl font-bold mt-2">

                    Happy

                  </h2>

                </div>

                <div className="flex items-center gap-4">

                  <ShieldCheck
                    className="text-green-600"
                    size={34}
                  />

                  <div>

                    <h3 className="font-bold">

                      Emergency Alert

                    </h3>

                    <p className="text-gray-500">

                      Immediate volunteer support.

                    </p>

                  </div>

                </div>

                <div className="bg-slate-100 rounded-xl p-4">

                  <p className="text-gray-600">

                    AI Recommendation

                  </p>

                  <p className="font-semibold mt-2">

                    Try a 10-minute guided breathing session today.

                  </p>

                </div>

              </div>

            </div>

          </motion.div>

        </div>

      </section>
    </FadeInSection>
  );
}