# normalisierte Gleitpunktzahlen
suppressPackageStartupMessages(library(mosaic))

all_values <- function(Z, E, B = 2, V=c("+", "-")) {
    ret <- c()
    for (e in E) {
        for (z in Z) {
            for (v in V) {
                val <-0
                b <- 0.5
                for (c in strsplit(z, NULL)[[1]]) {
                    if (c == "1") val <- val + b
                    b <- b * 0.5
                }
                val <- val*eval(parse(text=paste0(v,"1")))*eval(parse(text=paste(B,"**(",e,")")))
                ret <- c(ret, val)
            }
        }
    }
    c(0, ret)
}

plotVerteilung <- function(verteilung, limits=NULL, labels=NULL) {
    ggplot(verteilung, aes(x, fill=factor(normalized))) + 
        geom_dotplot(
            binwidth = 0.03,
            dotsize=1.2,
            stackgroups = TRUE,
            stackratio = 1.1,
            binpositions = "all",
            method = "histodot",
            show.legend = FALSE,
            stackdir="center"
        ) + 
        theme_minimal() + 
        scale_y_continuous(NULL, breaks = NULL) +
        scale_x_discrete(
            limits=limits, 
            labels=labels
        ) +
        ylab("")
}

B <- 2
E <- c("-1","0","1")
Z <- c("100", "101", "110", "111")
V <- c("+", "-")

#B <- 2
#E <- c("-1","0","1","2")
#Z <- c("100", "101", "110", "111")
#V <- c("+", "-")


normValues <- all_values(Z, E, B, V)
normValues.len <- length(normValues)

NZ <- c("001", "010", "011", "000")
nonNormValues <- all_values(NZ, E, B, V)
nonNormValues.len <- length(nonNormValues)

allValues <- c(normValues, nonNormValues)
allValues.uniquiLength <- length(unique(allValues))

x_min <- round(min(allValues))
x_max <- round(max(allValues))

df <- data.frame( 
        x = allValues, 
        normalized = c(rep("yes", normValues.len), rep("no", nonNormValues.len))
)

lim_lab <- seq(x_min, x_max, 0.5)

plotVerteilung(df, limits=lim_lab, labels=lim_lab)

ggsave("VerteilungGleitpunktzahlen_all.pdf", device="pdf", width = 9, height = 1.5, units="in")

plotVerteilung(df[df$normalized == "yes",], limits=lim_lab, labels=lim_lab)

ggsave("VerteilungGleitpunktzahlen_norm.pdf", device="pdf", width = 9, height = 1.5, units="in")

plotVerteilung(df[df$normalized == "no",], limits=lim_lab, labels=lim_lab)

ggsave("VerteilungGleitpunktzahlen_nonnorm.pdf", device="pdf", width = 9, height = 1.5, units="in")









gf_point(rep(1, nrow(df)) ~ x, color = ~ normalized, data=df) %>%
    gf_lims(x = c(-4,4), y=c(0.99,1.01)) %>%
    gf_theme(theme_minimal())

bins <- length(unique(c(normValues,nonNormValues)))

gf_dotplot(~ x, fill = ~ normalized, binwidth=0.04, binpositions="all", show.legend=FALSE,
           method= "histodot", dotsize = 1, data=df) %>%
    gf_lims(x = c(-3.5, 3.5)) %>%
    gf_refine(scale_y_discrete(limits=c(0))) %>%
    gf_theme(theme_minimal())

gf_counts(~ x, fill = ~ normalized, size=2, show.legend=FALSE, geom="dotplot", data=df) %>%
    gf_lims(x = c(-3.5, 3.5)) %>%
    gf_theme(theme_minimal())

######
ggplot(df[df$normalized=="yes",], aes(x, 1, color=normalized)) + 
    geom_hline(yintercept = 1, size= 0.1) +
    geom_point(show.legend = FALSE) + 
    theme_minimal() +  
    scale_y_continuous(NULL, breaks = NULL) 
ggsave("VerteilungGleitpunktzahlen_norm.pdf", device="pdf", width = 9, height = 1.5, units="in")
ggplot(df[df$normalized=="no",], aes(x, 1, color=normalized)) + 
    geom_hline(yintercept = 1, size= 0.1) +
    geom_point(show.legend = FALSE) + 
    theme_minimal() +  
    scale_y_continuous(NULL, breaks = NULL) 
ggsave("VerteilungGleitpunktzahlen_nonnorm.pdf", device="pdf", width = 9, height = 1.5, units="in")
#####

ggplot(df[df$normalized=="yes",], aes(x, fill=factor(normalized))) + 
    geom_dotplot(
        binwidth = 0.03,
        dotsize=1.2,
        stackgroups = TRUE,
        stackratio = 1.1,
        binpositions = "all",
        method = "histodot",
        show.legend = FALSE,
        stackdir="center",
    ) + 
    theme_minimal() + 
    scale_y_continuous(NULL, breaks = NULL) +
    scale_x_discrete(
#        limits=c(-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5), 
#        labels=c("","-3", "", "-2","", "-1","", "0", "", "1" ,"", "2","", "3", "")
        #nice.breaks=F,
        breaks=c(-2,-1.5,-1,-0.5,0,0.5,1,1.5,2),
        labels=c("-2", "", "-1", "", "0", "", "1" ,"", "2"),
        limits=c(-2.5,2.5)
    ) +
    ylab("")

ggsave("VerteilungGleitpunktzahlen1.pdf", device="pdf", width = 9, height = 1.5, units="in")
