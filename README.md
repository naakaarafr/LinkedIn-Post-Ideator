# LinkedIn Post Ideator 🚀

An intelligent AI-powered system that automatically researches, writes, and refines engaging LinkedIn posts about emerging AI and technology skills. Built with CrewAI and powered by Google's Gemini 2.0 Flash model.

## 📋 Overview

This project uses a multi-agent system to create high-quality LinkedIn content through a three-stage process:

1. **Research Phase**: A Senior Career Coach agent researches emerging AI/tech skills
2. **Content Creation**: A LinkedIn Influencer Writer creates engaging posts
3. **Quality Assurance**: An Expert Writing Critic refines and polishes the content

## 🎯 Features

- **Automated Research**: Discovers trending AI and technology skills for 2025
- **Optimized Content**: Creates LinkedIn posts under 200 words with emojis and hashtags
- **Quality Control**: Built-in review and refinement process
- **SEO-Friendly**: Includes relevant hashtags and engaging headlines
- **Professional Focus**: Targets tech professionals and career development

## 🏗️ Architecture

The system consists of three specialized AI agents:

### 🎓 Senior Career Coach
- **Role**: Research and trend analysis
- **Goal**: Discover key tech and AI career skills for 2025
- **Tools**: Web search capabilities via SerperDev
- **Output**: Comprehensive skill reports with actionable insights

### ✍️ LinkedIn Influencer Writer  
- **Role**: Content creation
- **Goal**: Write catchy, emoji-filled LinkedIn posts (max 200 words)
- **Specialty**: AI and technology focused content
- **Output**: Engaging LinkedIn posts with headlines and hashtags

### 🔍 Expert Writing Critic
- **Role**: Quality assurance and refinement
- **Goal**: Provide constructive feedback and polish content
- **Focus**: Ensures posts are concise, engaging, and platform-optimized
- **Output**: Final, publication-ready LinkedIn posts

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Google API Key (for Gemini 2.0 Flash)
- SerperDev API Key (for web search)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/naakaarafr/linkedin-post-ideator.git
   cd linkedin-post-ideator
   ```

2. **Install dependencies**
   ```bash
   pip install crewai
   pip install langchain-google-genai
   pip install crewai-tools
   pip install python-dotenv
   ```

3. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

4. **API Keys Setup**
   - **Google API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **SerperDev API Key**: Get from [SerperDev](https://serper.dev/)

## 🚀 Usage

### Basic Usage
```bash
python crew.py
```

### What Happens When You Run It

1. **Research Phase**: The Career Coach agent searches for emerging AI/tech skills
2. **Content Creation**: The Influencer Writer creates a LinkedIn post based on research
3. **Quality Review**: The Critic agent reviews and refines the post
4. **Output**: Final polished LinkedIn post ready for publishing

### Expected Output Format

```
🚀 Top AI Skills for 2025!

The tech landscape is evolving rapidly! Here are the must-have skills:

🤖 Prompt Engineering - Master AI communication
🔍 Vector Databases - Power next-gen search
⚡ Edge AI - Bring intelligence to devices
🛡️ AI Safety - Ensure responsible development
📊 Multimodal AI - Work with text, image, and audio

Ready to future-proof your career? Start with one skill this week! 💪

#AI2025 #TechSkills #CareerDevelopment #ArtificialIntelligence #FutureOfWork
```

## 📁 Project Structure

```
linkedin-post-ideator/
├── agents.py          # AI agent definitions
├── tasks.py           # Task configurations
├── tools.py           # Search tool setup  
├── crew.py            # Main execution script
├── .env               # Environment variables
├── requirements.txt   # Dependencies
└── README.md          # This file
```

## 🔧 Configuration

### Agent Customization

You can modify agent behavior by editing `agents.py`:

- **Temperature**: Adjust creativity (0.0-1.0)
- **Roles & Goals**: Customize agent specializations  
- **Backstories**: Fine-tune agent personalities

### Task Modification

Customize output requirements in `tasks.py`:

- **Post Length**: Modify word count limits
- **Content Focus**: Change research topics
- **Format Requirements**: Adjust emoji/hashtag rules

## 📈 Advanced Features

### Sequential Processing
The system uses CrewAI's sequential process to ensure:
- Research completion before content creation
- Content creation before criticism
- Proper context passing between agents

### Error Handling
Built-in exception handling ensures:
- Graceful failure recovery
- Detailed error reporting
- System stability

## 🤝 Contributing

Created by [@naakaarafr](https://github.com/naakaarafr)

Feel free to:
- Submit issues and feature requests
- Fork the repository and create pull requests
- Share your improvements and customizations

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🚨 Important Notes

- **API Costs**: Be mindful of API usage costs for Google Gemini and SerperDev
- **Rate Limits**: Respect API rate limits to avoid service interruptions
- **Content Review**: Always review generated content before publishing
- **Compliance**: Ensure posts comply with LinkedIn's terms of service

## 🔮 Future Enhancements

- [ ] Support for multiple social platforms
- [ ] Custom skill category targeting
- [ ] Scheduled post generation
- [ ] Analytics integration
- [ ] Multiple language support
- [ ] Template customization UI

## 📞 Support

For questions, issues, or contributions:
- GitHub Issues: [Create an issue](https://github.com/naakaarafr/linkedin-post-ideator/issues)
- Email: Contact via GitHub profile

---

**Built with ❤️ using CrewAI and Google Gemini 2.0 Flash**

*Empowering professionals to share knowledge and grow their careers through AI-powered content creation.*
