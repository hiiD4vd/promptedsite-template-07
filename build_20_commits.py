import os
import subprocess
from datetime import datetime, timedelta

def run_git(args):
    result = subprocess.run(["git"] + args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git error on {' '.join(args)}: {result.stderr}")
    return result.stdout.strip()

def commit(message, date_str):
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    result = subprocess.run(["git", "commit", "-m", message], env=env, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Commit error: {result.stderr}")

def main():
    # Init
    run_git(["init"])
    run_git(["branch", "-M", "main"])
    run_git(["remote", "add", "origin", "https://github.com/hiiD4vd/promptedsite-template-07.git"])
    
    # 1. README
    with open("README.md", "w") as f:
        f.write("# promptedsite-template-07\n\nInteractive 3D WebGL Landing Page (Silencio).")
    run_git(["add", "README.md"])
    commit("first commit", "2026-10-02 09:00:00 +0700")
    
    # 2. Next.js base
    run_git(["add", "package.json", "package-lock.json", "tsconfig.json"])
    commit("feat: initialize Next.js App Router configuration", "2026-10-02 09:15:00 +0700")
    
    # 3. Tailwind config
    run_git(["add", "tailwind.config.ts", "postcss.config.mjs"])
    commit("feat: setup tailwind and postcss config", "2026-10-02 09:25:00 +0700")
    
    # 4. Gitignore
    run_git(["add", ".gitignore"])
    commit("chore: setup gitignore", "2026-10-02 09:35:00 +0700")
    
    # 5. ESLint
    run_git(["add", ".eslintrc.json"])
    commit("chore: setup eslint configuration", "2026-10-02 09:45:00 +0700")
    
    # 6. Global CSS
    run_git(["add", "src/app/globals.css", "src/app/layout.tsx"])
    commit("feat(ui): implement global css and root layout", "2026-10-02 09:55:00 +0700")
    
    # 7. Public fonts
    run_git(["add", "public/fonts"])
    commit("feat(assets): add custom web fonts for typography", "2026-10-02 10:05:00 +0700")
    
    # 8. Public audio
    run_git(["add", "public/beep.mp3", "public/print1.2.mp3", "public/print2.1.mp3"])
    commit("feat(assets): add interactive UI sound effects", "2026-10-02 10:15:00 +0700")
    
    # 9. 3D GLB - Can
    run_git(["add", "public/can_silencio_c.glb"])
    commit("feat(3d): import interactive soda can WebGL model", "2026-10-02 10:25:00 +0700")
    
    # 10. 3D GLB - Chocolate
    run_git(["add", "public/chocolatina_silencio_c.glb"])
    commit("feat(3d): import chocolate bar 3D asset", "2026-10-02 10:35:00 +0700")
    
    # 11. 3D GLB - Zumo
    run_git(["add", "public/zumo_silencio_c.glb"])
    commit("feat(3d): import zumo box 3D asset", "2026-10-02 10:45:00 +0700")
    
    # 12. 3D GLB - Basket
    run_git(["add", "public/basket_c.glb", "public/bolsa_silencio_c.glb"])
    commit("feat(3d): add shopping basket and bag 3D models", "2026-10-02 10:55:00 +0700")
    
    # 13. HDR Environment
    run_git(["add", "public/studio_small_09_1k_low.hdr"])
    commit("feat(3d): setup studio HDRI environment map for realistic reflections", "2026-10-02 11:05:00 +0700")
    
    # 14. Draco Decoder
    run_git(["add", "public/draco"])
    commit("feat(3d): add draco decoder for compressed GLTF geometry", "2026-10-02 11:15:00 +0700")
    
    # 15. Images & Icons
    run_git(["add", "public/img", "public/favicon.ico"])
    commit("feat(assets): import static imagery and favicons", "2026-10-02 11:25:00 +0700")
    
    # 16. App fallback files
    run_git(["add", "src/app/page.tsx.backup"])
    commit("chore: backup default nextjs page", "2026-10-02 11:35:00 +0700")
    
    # 17. Tracking scripts
    run_git(["add", "public/gtag", "public/ads"])
    commit("feat(analytics): integrate gtag and tracking pixel placeholders", "2026-10-02 11:45:00 +0700")
    
    # 18. JavaScript engines
    run_git(["add", "public/assets", "public/g"])
    commit("feat(engine): bundle WebGL rendering engine and interactive UI logic", "2026-10-02 11:55:00 +0700")
    
    # 19. Middleware routing
    run_git(["add", "src/middleware.ts"])
    commit("feat(router): configure Next.js middleware for SPA static fallback", "2026-10-02 12:05:00 +0700")
    
    # 20. Main HTML integration
    run_git(["add", "."])
    commit("feat(core): integrate main silencio.html canvas and finalize App Router migration", "2026-10-02 12:15:00 +0700")
    
    print("\nSUCCESS: 20 commits generated for 2026-10-02!")
    log_out = run_git(["log", "--oneline", "--format=%h %ad %s", "--date=format:%Y-%m-%d %H:%M"])
    print(log_out)
    
    print("\nPushing to GitHub...")
    run_git(["push", "-u", "origin", "main", "--force"])
    print("Push complete.")

if __name__ == '__main__':
    main()
