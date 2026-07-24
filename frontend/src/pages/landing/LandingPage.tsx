import LandingNavbar from "@/components/landing/LandingNavbar";
import Hero from "@/components/landing/Hero";
import Stats from "@/components/landing/Stats";
import Features from "@/components/landing/Features";
import HowItWorks from "@/components/landing/HowItWorks";
import DashboardPreview from "@/components/landing/DashboardPreview";
import ChatbotPreview from "@/components/landing/ChatbotPreview";
import About from "@/components/landing/About";
import FAQ from "@/components/landing/FAQ";
import CTA from "@/components/landing/CTA";
import Footer from "@/components/landing/Footer";

import FadeInSection from "@/components/common/FadeInSection";

export default function LandingPage() {
  return (
    <>
      <LandingNavbar />

      <Hero />

      <FadeInSection>
        <Stats />
      </FadeInSection>

      <FadeInSection>
        <Features />
      </FadeInSection>

      <FadeInSection>
        <HowItWorks />
      </FadeInSection>

      <FadeInSection>
        <DashboardPreview />
      </FadeInSection>

      <FadeInSection>
        <ChatbotPreview />
      </FadeInSection>

      <FadeInSection>
        <About />
      </FadeInSection>

      <FadeInSection>
        <FAQ />
      </FadeInSection>

      <FadeInSection>
        <CTA />
      </FadeInSection>

      <FadeInSection>
        <Footer />
      </FadeInSection>
    </>
  );
}