import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import ContHarb from "./shared/ContHarb";

const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>Content Harbor | AI Social Media Assistant</title>
        <meta
          name="description"
          content="Generate content snippets for your posts."
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <ContHarb />
    </div>
  );
};

export default Home;