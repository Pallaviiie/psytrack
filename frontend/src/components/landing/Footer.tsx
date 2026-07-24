import {
  BrainCircuit,
  Mail,
  Phone,
  MapPin,
} from "lucide-react";

export default function Footer() {
  return (
    <footer className="bg-slate-950 text-gray-300">

      <div className="max-w-7xl mx-auto px-6 py-16">

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-10">

          {/* Brand */}

          <div>

            <div className="flex items-center gap-3 mb-5">

              <BrainCircuit
                className="text-violet-500"
                size={34}
              />

              <div>
                <h2 className="text-2xl font-bold text-white">
                  PsyTrack
                </h2>

                <p className="text-sm text-gray-400">
                  AI Mental Health
                </p>

              </div>

            </div>

            <p className="leading-7 text-gray-400">
              PsyTrack is an AI-powered mental wellness platform
              that helps users monitor emotional health through
              intelligent assessments, chatbot conversations,
              personalized recommendations and emergency alerts.
            </p>

          </div>

          {/* Quick Links */}

          <div>

            <h3 className="text-white font-semibold text-lg mb-5">
              Quick Links
            </h3>

            <ul className="space-y-3">

              <li>
                <a href="#features" className="hover:text-violet-400">
                  Features
                </a>
              </li>

              <li>
                <a href="#how" className="hover:text-violet-400">
                  How It Works
                </a>
              </li>

              <li>
                <a href="#about" className="hover:text-violet-400">
                  About Us
                </a>
              </li>

              <li>
                <a href="#faq" className="hover:text-violet-400">
                  FAQ
                </a>
              </li>

            </ul>

          </div>

          {/* Services */}

          <div>

            <h3 className="text-white font-semibold text-lg mb-5">
              Services
            </h3>

            <ul className="space-y-3">

              <li>✔ Mental Health Assessment</li>

              <li>✔ AI Chatbot</li>

              <li>✔ Personalized Recommendations</li>

              <li>✔ Emergency Alert System</li>

              <li>✔ Wellness Tracking Dashboard</li>

            </ul>

          </div>

          {/* Contact */}

          <div>

            <h3 className="text-white font-semibold text-lg mb-5">
              Contact
            </h3>

            <div className="space-y-4">

              <div className="flex items-center gap-3">

                <Mail size={18} />

                support@psytrack.ai

              </div>

              <div className="flex items-center gap-3">

                <Phone size={18} />

                +91 91204 88711

              </div>

              <div className="flex items-center gap-3">

                <MapPin size={18} />

                Greater Noida, India

              </div>

            </div>

          </div>

        </div>

        {/* Bottom */}

        <div className="border-t border-slate-800 mt-12 pt-6 flex flex-col md:flex-row justify-between items-center gap-4">

          <p className="text-sm text-gray-500">

            © 2026 PsyTrack. All Rights Reserved.

          </p>

          <p className="flex items-center gap-2 text-sm text-gray-500">

            Designed by Pallavi, Saloni & Pragya

          </p>

        </div>

      </div>

    </footer>
  );
}