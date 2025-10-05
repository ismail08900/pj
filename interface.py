import tkinter as tk
from tkinter import ttk, messagebox
from sauvegarde import sauvegarder, charger
from medias import Media
from bibliotheque import Bibliotheque

# ------------------------------
# Interface de Connexion avant lancer_app
# ------------------------------
def verifier_login():
    nom = champ_nom.get()
    mdp = champ_mdp.get()

    utilisateurs = {
        "admin": "1234",
        "oussama": "azerty"
    }

    if nom in utilisateurs and utilisateurs[nom] == mdp:
        fen_login.destroy()
        lancer_app()
    else:
        messagebox.showerror("Erreur", "Nom ou mot de passe incorrect.")

fen_login = tk.Tk()
fen_login.title("🔐 Connexion")
fen_login.geometry("400x300")
fen_login.configure(bg="#ECEFF1")

tk.Label(fen_login, text="Connexion", font=("Segoe UI", 20, "bold"), bg="#ECEFF1", fg="#0D47A1").pack(pady=20)
tk.Label(fen_login, text="Nom d'utilisateur:", bg="#ECEFF1", font=("Segoe UI", 12)).pack()
champ_nom = tk.Entry(fen_login, font=("Segoe UI", 12), width=30)
champ_nom.pack(pady=5)

tk.Label(fen_login, text="Mot de passe:", bg="#ECEFF1", font=("Segoe UI", 12)).pack()
champ_mdp = tk.Entry(fen_login, show="*", font=("Segoe UI", 12), width=30)
champ_mdp.pack(pady=5)

tk.Button(fen_login, text="Se connecter", command=verifier_login,
          font=("Segoe UI", 12, "bold"), bg="#1565C0", fg="white", padx=15, pady=5).pack(pady=20)

# ------------------------------
# Traductions et classes Media / Bibliotheque
# ------------------------------
traductions = {
    "fr": {
        "type_media": "Type de média:",
        "champs": ['Titre', 'Genre', 'Année', 'Auteur/Réalisateur/Artiste', 'Pages/Durée'],
        "ajouter": "Ajouter",
        "rechercher": "Rechercher",
        "supprimer": "Supprimer sélection",
        "modifier": "Modifier",
        "langue": "Langue",
        "aucun_media": "Aucun média trouvé.",
        "erreur_champs": "Veuillez remplir tous les champs.",
        "erreur_nombre": "Année et Pages/Durée doivent être des nombres.",
        "attention_sel": "Veuillez sélectionner un média à supprimer.",
        "confirmer_suppr": "Voulez-vous vraiment supprimer « {} » ?",
        "titre_vide": "Veuillez saisir un titre pour la recherche.",
        "auteur_label": {
            "Livre": "Auteur",
            "Film": "Réalisateur",
            "Musique": "Artiste"
        }
    },
    "en": {
        "type_media": "Media type:",
        "champs": ['Title', 'Genre', 'Year', 'Author/Director/Artist', 'Pages/Duration'],
        "ajouter": "Add",
        "rechercher": "Search",
        "supprimer": "Delete selection",
        "modifier": "Update",
        "langue": "Language",
        "aucun_media": "No media found.",
        "erreur_champs": "Please fill all fields.",
        "erreur_nombre": "Year and Pages/Duration must be numbers.",
        "attention_sel": "Please select a media to delete.",
        "confirmer_suppr": "Do you really want to delete « {} »?",
        "titre_vide": "Please enter a title to search.",
        "auteur_label": {
            "Livre": "Author",
            "Film": "Director",
            "Musique": "Artist"
        }
    },
    "ar": {
        "type_media": "نوع الوسيط:",
        "champs": ['العنوان', 'النوع', 'السنة', 'المؤلف/المخرج/الفنان', 'الصفحات/المدة'],
        "ajouter": "إضافة",
        "rechercher": "بحث",
        "supprimer": "حذف المحدد",
        "modifier": "تعديل",
        "langue": "اللغة",
        "aucun_media": "لا يوجد وسائط.",
        "erreur_champs": "يرجى ملء جميع الحقول.",
        "erreur_nombre": "السنة والصفحات/المدة يجب أن تكون أرقاماً.",
        "attention_sel": "يرجى اختيار وسيط للحذف.",
        "confirmer_suppr": "هل تريد حقاً حذف « {} »؟",
        "titre_vide": "يرجى إدخال عنوان للبحث.",
        "auteur_label": {
            "Livre": "المؤلف",
            "Film": "المخرج",
            "Musique": "الفنان"
        }
    }
}

class Media:
    def __init__(self, titre, genre, annee, personne, nb):
        self.titre = titre
        self.genre = genre
        self.annee = annee
        self.personne = personne
        self.nb = nb

class Bibliotheque:
    def __init__(self):
        self.medias = []

    def ajouter_media(self, media):
        self.medias.append(media)

    def get_tous(self):
        return self.medias

    def rechercher(self, titre):
        return [m for m in self.medias if titre.lower() in m.titre.lower()]

    def supprimer_media(self, titre):
        self.medias = [m for m in self.medias if m.titre != titre]

    def modifier_media(self, ancien_titre, nouveau_media):
        for i, media in enumerate(self.medias):
            if media.titre == ancien_titre:
                self.medias[i] = nouveau_media
                return True
        return False

current_lang = "fr"

# ------------------------------
# Interface principale (bibliothèque multimédia)
# ------------------------------
def lancer_app():
    bib = Bibliotheque()
    bib.medias = charger()  # Charger les médias sauvegardés

    fen = tk.Tk()
    fen.title("📚 Bibliothèque Multimédia Moderne")
    fen.geometry("900x540")

    style = ttk.Style()
    style.theme_use("clam")

    theme_dark = True

    def config_styles(dark=True):
        if dark:
            fen.configure(bg="#121212")
            style.configure("TLabel", background="#121212", foreground="white", font=("Segoe UI", 11))
            style.configure("TEntry", fieldbackground="#333333", foreground="#eeeeee", font=("Segoe UI", 11))
            style.configure("TButton", background="#6200EE", foreground="white", font=("Segoe UI", 11, "bold"))
            style.configure("Treeview", background="#222222", foreground="white", fieldbackground="#222222", font=("Consolas", 11))
            style.map('Treeview', background=[('selected', '#6200EE')], foreground=[('selected', 'white')])
            label_type.configure(background="#121212", foreground="white")
            label_langue.configure(background="#121212", foreground="white")
            for lab in labels_champs:
                lab.configure(background="#121212", foreground="white")
            btn_theme.config(text="Mode Clair")
        else:
            fen.configure(bg="#f0f0f0")
            style.configure("TLabel", background="#f0f0f0", foreground="#222222", font=("Segoe UI", 11))
            style.configure("TEntry", fieldbackground="white", foreground="black", font=("Segoe UI", 11))
            style.configure("TButton", background="#1976D2", foreground="white", font=("Segoe UI", 11, "bold"))
            style.configure("Treeview", background="white", foreground="black", fieldbackground="white", font=("Consolas", 11))
            style.map('Treeview', background=[('selected', '#1976D2')], foreground=[('selected', 'white')])
            label_type.configure(background="#f0f0f0", foreground="#222222")
            label_langue.configure(background="#f0f0f0", foreground="#222222")
            for lab in labels_champs:
                lab.configure(background="#f0f0f0", foreground="#222222")
            btn_theme.config(text="Mode Sombre")

    var_type = tk.StringVar(value="Livre")

    label_type = ttk.Label(fen, text=traductions[current_lang]["type_media"])
    label_type.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    combo_type = ttk.Combobox(fen, textvariable=var_type, values=["Livre", "Film", "Musique"], state="readonly")
    combo_type.grid(row=0, column=1, padx=10, pady=10)

    champs_keys = ['Titre', 'Genre', 'Année', 'Auteur/Réalisateur/Artiste', 'Pages/Durée']
    champs = traductions[current_lang]["champs"]

    labels_champs = []
    entrees = {}

    for i, champ in enumerate(champs, start=1):
        lab = ttk.Label(fen, text=champ + ":")
        lab.grid(row=i, column=0, padx=10, pady=6, sticky="w")
        labels_champs.append(lab)
        e = ttk.Entry(fen, width=40)
        e.grid(row=i, column=1, padx=10, pady=6)
        entrees[champs_keys[i-1]] = e

    columns = champs_keys

    tree = ttk.Treeview(fen, columns=columns, show="headings", height=12)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    tree.grid(row=7, column=0, columnspan=5, padx=10, pady=15, sticky="nsew")

    scrollbar = ttk.Scrollbar(fen, orient="vertical", command=tree.yview)
    scrollbar.grid(row=7, column=5, sticky="ns", pady=15)
    tree.configure(yscrollcommand=scrollbar.set)

    btn_ajouter = ttk.Button(fen, text=traductions[current_lang]["ajouter"])
    btn_rechercher = ttk.Button(fen, text=traductions[current_lang]["rechercher"])
    btn_supprimer = ttk.Button(fen, text=traductions[current_lang]["supprimer"])
    btn_modifier = ttk.Button(fen, text=traductions[current_lang]["modifier"])
    btn_theme = ttk.Button(fen, text="Mode Clair")

    btn_ajouter.grid(row=8, column=0, padx=12, pady=12, sticky="ew")
    btn_rechercher.grid(row=8, column=1, padx=12, pady=12, sticky="ew")
    btn_supprimer.grid(row=8, column=2, padx=12, pady=12, sticky="ew")
    btn_modifier.grid(row=8, column=3, padx=12, pady=12, sticky="ew")
    btn_theme.grid(row=8, column=4, padx=12, pady=12, sticky="ew")

    label_langue = ttk.Label(fen, text=traductions[current_lang]["langue"])
    label_langue.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    combo_langue = ttk.Combobox(fen, values=list(traductions.keys()), width=5, state="readonly")
    combo_langue.set(current_lang)
    combo_langue.grid(row=0, column=3, padx=10, pady=10)

    def afficher(medias=None):
        tree.delete(*tree.get_children())
        if medias is None:
            medias = bib.get_tous()
        if not medias:
            messagebox.showinfo("Info", traductions[current_lang]["aucun_media"])
        else:
            for m in medias:
                tree.insert("", "end", values=(m.titre, m.genre, m.annee, m.personne, m.nb))

    def maj_label_auteur():
        type_sel = var_type.get()
        nouveau_label = traductions[current_lang]["auteur_label"][type_sel]
        labels_champs[3].config(text=nouveau_label + ":")

    def clear_inputs():
        for entry in entrees.values():
            entry.delete(0, tk.END)

    def ajouter():
        try:
            t = entrees['Titre'].get()
            g = entrees['Genre'].get()
            a = int(entrees['Année'].get())
            pers = entrees['Auteur/Réalisateur/Artiste'].get()
            nb = int(entrees['Pages/Durée'].get())

            if not t or not g or not pers:
                messagebox.showerror("Erreur", traductions[current_lang]["erreur_champs"])
                return

            media = Media(t, g, a, pers, nb)
            bib.ajouter_media(media)
            sauvegarder(bib.get_tous())
            afficher()
            clear_inputs()
        except ValueError:
            messagebox.showerror("Erreur", traductions[current_lang]["erreur_nombre"])

    def rechercher():
        titre = entrees['Titre'].get()
        if not titre:
            messagebox.showwarning("Attention", traductions[current_lang]["titre_vide"])
            return
        resultats = bib.rechercher(titre)
        if not resultats:
            messagebox.showinfo("Info", traductions[current_lang]["aucun_media"])
        afficher(resultats)
        clear_inputs()

    def supprimer():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Attention", traductions[current_lang]["attention_sel"])
            return
        item = sel[0]
        values = tree.item(item, "values")
        titre = values[0]
        if messagebox.askyesno("Confirmer", traductions[current_lang]["confirmer_suppr"].format(titre)):
            bib.supprimer_media(titre)
            sauvegarder(bib.get_tous())
            afficher()
            clear_inputs()

    def modifier():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Attention", traductions[current_lang]["attention_sel"])
            return

        item = sel[0]
        values = tree.item(item, "values")
        ancien_titre = values[0]

        try:
            t = entrees['Titre'].get()
            g = entrees['Genre'].get()
            a = int(entrees['Année'].get())
            pers = entrees['Auteur/Réalisateur/Artiste'].get()
            nb = int(entrees['Pages/Durée'].get())

            if not t or not g or not pers:
                messagebox.showerror("Erreur", traductions[current_lang]["erreur_champs"])
                return

            nouveau = Media(t, g, a, pers, nb)
            ok = bib.modifier_media(ancien_titre, nouveau)
            if ok:
                sauvegarder(bib.get_tous())
                afficher()
                clear_inputs()
            else:
                messagebox.showerror("Erreur", "Média non trouvé pour modification.")
        except ValueError:
            messagebox.showerror("Erreur", traductions[current_lang]["erreur_nombre"])

    def remplir_inputs(event):
        sel = tree.selection()
        if not sel:
            return
        item = sel[0]
        values = tree.item(item, "values")

        champs_temp = ['Titre', 'Genre', 'Année', 'Auteur/Réalisateur/Artiste', 'Pages/Durée']
        for i, key in enumerate(champs_temp):
            entrees[key].delete(0, tk.END)
            entrees[key].insert(0, values[i])

    def changer_langue(event):
        nonlocal champs
        global current_lang
        current_lang = combo_langue.get()

        label_type.config(text=traductions[current_lang]["type_media"])
        champs = traductions[current_lang]["champs"]
        for i, lab in enumerate(labels_champs):
            lab.config(text=champs[i] + ":")
        btn_ajouter.config(text=traductions[current_lang]["ajouter"])
        btn_rechercher.config(text=traductions[current_lang]["rechercher"])
        btn_supprimer.config(text=traductions[current_lang]["supprimer"])
        btn_modifier.config(text=traductions[current_lang]["modifier"])
        label_langue.config(text=traductions[current_lang]["langue"])

        maj_label_auteur()

    def on_type_change(event):
        maj_label_auteur()

    def toggle_theme():
        nonlocal theme_dark
        theme_dark = not theme_dark
        config_styles(theme_dark)

    def on_enter(e):
        e.widget.configure(style="Hover.TButton")

    def on_leave(e):
        e.widget.configure(style="TButton")

    style.configure("Hover.TButton",
                    background="#03DAC5",
                    foreground="#000000",
                    font=("Segoe UI", 11, "bold"))

    combo_langue.bind("<<ComboboxSelected>>", changer_langue)
    combo_type.bind("<<ComboboxSelected>>", on_type_change)
    tree.bind("<<TreeviewSelect>>", remplir_inputs)
    btn_ajouter.config(command=ajouter)
    btn_rechercher.config(command=rechercher)
    btn_supprimer.config(command=supprimer)
    btn_modifier.config(command=modifier)
    btn_theme.config(command=toggle_theme)

    for btn in [btn_ajouter, btn_rechercher, btn_supprimer, btn_modifier, btn_theme]:
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    maj_label_auteur()
    config_styles(theme_dark)
    afficher()

    fen.mainloop()

fen_login.mainloop()
