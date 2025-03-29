import streamlit as st
import time
import random

def main():
    st.set_page_config(page_title="💖 Para Elena", page_icon="💌")
    
    # Estilos CSS personalizados
    st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to bottom right, #fff0f5, #ffb6c1);
        text-align: center;
    }
    .title {
        font-size: 3em !important;
        color: #8b0000 !important;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .heart {
        font-size: 2em;
        animation: beat 1s infinite;
    }
    @keyframes beat {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    .romantic-text {
        font-size: 1.5em;
        margin: 20px 0;
        line-height: 2;
    }
    </style>
    """, unsafe_allow_html=True)

    # Inicializa estados da sessão
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.name = ""
        st.session_state.answers = []

    # Passo 0: Pede o nome
    if st.session_state.step == 0:
        st.title("💖 Bem-vinda ao Jogo do Amor 💖")
        st.write("Antes de começar, qual é o seu nome?")
        
        name = st.text_input("Digite seu nome:")
        
        if st.button("Continuar") and name:
            if name.lower() != "elena":
                st.warning("Hmm, esse nome não parece correto... Tente novamente!")
            else:
                st.session_state.name = name
                st.session_state.step = 1
                st.rerun()

    # Passo 1: Primeira pergunta
    elif st.session_state.step == 1:
        st.title(f"Olá, {st.session_state.name}! ❤️")
        st.write("Vamos começar com uma pergunta fácil...")
        
        answer = st.radio(
            "O que você prefere?",
            ["Flores", "Chocolate", "Abraços", "Todos os anteriores"],
            index=None
        )
        
        if st.button("Próxima Pergunta") and answer:
            st.session_state.answers.append(answer)
            st.session_state.step = 2
            st.rerun()

    # Passo 2: Segunda pergunta
    elif st.session_state.step == 2:
        st.title("Segunda Pergunta 💭")
        
        answer = st.radio(
            "Qual é o seu momento favorito do dia?",
            ["Manhã", "Tarde", "Noite", "Qualquer hora contigo"],
            index=None
        )
        
        if st.button("Próxima Pergunta") and answer:
            st.session_state.answers.append(answer)
            st.session_state.step = 3
            st.rerun()

    # Passo 3: Terceira pergunta
    elif st.session_state.step == 3:
        st.title("Última Pergunta 🎀")
        
        answer = st.radio(
            "Como você descreveria o amor perfeito?",
            ["Aventura", "Companheirismo", "Paixão", "Tudo isso e mais um pouco"],
            index=None
        )
        
        if st.button("Ver Resultado") and answer:
            st.session_state.answers.append(answer)
            st.session_state.step = 4
            st.rerun()

    # Passo 4: Revelação do presente
    elif st.session_state.step == 4:
        st.title("🎉 Parabéns, Elena! 🎉")
        st.write("Você completou todas as perguntas!")
        st.write("Com base nas suas respostas, você ganhou um presente especial!")
        
        if st.button("Clique aqui para descobrir", key="surprise_button"):
            st.session_state.step = 5
            st.rerun()

    # Passo 5: Pedido de namoro
    elif st.session_state.step == 5:
        st.markdown('<p class="title">Elena, quer namorar comigo?</p>', unsafe_allow_html=True)
        
        # Efeito de corações
        heart_container = st.empty()
        hearts = "💖💗💓💞💕💘💝💟"
        for _ in range(10):  # Reduzi para 10 iterações para ser mais rápido
            heart_container.markdown(f'<div class="heart">{random.choice(hearts)}</div>', unsafe_allow_html=True)
            time.sleep(0.3)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("SIM! 💖", use_container_width=True, key="yes_button"):
                st.session_state.step = 6
                st.rerun()
        
        with col2:
            if st.button("Não 😢", use_container_width=True, key="no_button"):
                st.session_state.step = 7
                st.rerun()

    # Passo 6: Resposta positiva
    elif st.session_state.step == 6:
        st.balloons()
        st.markdown('<p class="title">💝 A partir de agora te prometo que vou te fazer a mulher mais feliz do mundo! 💝</p>', unsafe_allow_html=True)
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3Axejg3ZGNrOWV3b2tqbzBlaWZ5bHVoZmp6dzA3d21sbHNqYzRnMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l49K0VSPusJDkPOOk/giphy.gif", width=400)
        st.markdown("""
        <div class="romantic-text">
        ❤️ Cada dia ao seu lado será especial <br>
        💖 Prometo te amar e cuidar de você <br>
        🌟 Você é a melhor coisa que me aconteceu
        </div>
        """, unsafe_allow_html=True)

    # Passo 7: Resposta negativa
    elif st.session_state.step == 7:
        st.error("Por favor, reconsidera... 😢💔")
        st.image("amor.gif", width=400)
        
        if st.button("Voltar", key="back_button"):
            st.session_state.step = 5
            st.rerun()

if __name__ == "__main__":
    main()